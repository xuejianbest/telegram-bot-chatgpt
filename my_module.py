# tg user_id
tg_bot_whitelist= []

TG_BOT_TOKEN = ''
GPT_API_KEY = ''

TG_BOT_TOKEN_1 = ''
GPT_ACCESS_TOKEN = ''
########### ########## ############

def check_quotes(s):
    backticks = s.count('```')
    single_quotes = s.count('`') - 3 * backticks
    if backticks % 2 == 1:
        s += '\n```'
    if single_quotes % 2 == 1:
        s += '`'
    return s

def escape_string(s):
    s = check_quotes(s)
    result = ''
    in_backtick = False
    double_star = False
    for i in range(len(s)):
        if double_star:
            double_star = False
            continue
        if s[i] == '`':
            in_backtick = not in_backtick
            result += '`'
        elif s[i] == '*':
            if in_backtick:
                result += '*'
            else:
                if i < len(s) - 1 and s[i+1] == '*':
                    result += '*'
                    double_star = True
                else:
                    result += '_'
        elif s[i] == '_':
            if in_backtick:
                result += '_'
            else:
                result += '\\_'
        else:
            result += s[i]
    return result
