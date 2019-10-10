# Для каждого слова из данного текста https://ru.lipsum.com/feed/html подсчитайте,
# сколько раз оно встречалось в этом тексте ранее.
# Результат в виде словаря
Text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce libero neque, dignissim tincidunt mattis 
vel, rhoncus in dui. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. 
Aliquam et erat ac dolor porttitor efficitur. Ut in neque non lorem fringilla facilisis at vel nibh. Nam sed blandit 
eros, fringilla porttitor nisl. Ut turpis lectus, consequat ut tortor ac, auctor condimentum enim. Aenean a lacus 
ornare, ornare magna quis, ultricies metus. 

Phasellus ac mauris nec magna dictum sodales. Vestibulum vulputate, dui at sollicitudin tempus, lorem est ullamcorper 
leo, ut viverra orci felis et nunc. Phasellus lorem nulla, placerat nec risus eget, porttitor volutpat libero. 
Quisque tempus, nisl sit amet congue faucibus, libero mi pharetra sem, tempus suscipit lacus libero nec lacus. 
Aliquam eleifend tortor nec libero consequat pulvinar. Etiam vitae pellentesque nibh. Cras egestas nisl eu mi 
sollicitudin, at ornare erat luctus. In vitae tellus sit amet dolor imperdiet tempus in at lorem. Proin interdum 
purus et tortor rutrum, at faucibus sem iaculis. Suspendisse viverra quam a tempus ultricies. Curabitur nec diam ex. 
Duis pretium ornare leo ac molestie. Pellentesque laoreet dignissim libero. Etiam malesuada mi et arcu mollis, 
sit amet auctor orci molestie. 

Pellentesque in malesuada nibh. Praesent pulvinar molestie nisl nec elementum. Phasellus convallis elementum odio et 
convallis. Aliquam dapibus, magna at congue venenatis, turpis augue iaculis orci, sit amet rutrum lorem felis et 
orci. Mauris eget porta ante. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos 
himenaeos. Nam aliquet tortor nec tristique mollis. Nullam vehicula suscipit sapien, non fringilla purus ultricies 
ac. Interdum et malesuada fames ac ante ipsum primis in faucibus. Class aptent taciti sociosqu ad litora torquent per 
conubia nostra, per inceptos himenaeos. Integer lobortis, tellus sed dapibus bibendum, felis arcu imperdiet sapien, 
nec ultricies augue purus non ligula. Nam vitae bibendum massa, sit amet vehicula eros. Nullam lacinia viverra 
vestibulum. Duis nibh massa, placerat at hendrerit ac, molestie vitae dolor. Sed dignissim ex vitae malesuada 
scelerisque. Vestibulum tincidunt ipsum enim, eget blandit massa vulputate sit amet. 

Sed ut bibendum tortor, eget ullamcorper mi. Suspendisse quis porttitor ipsum, et pretium lacus. Duis malesuada eros 
eu ligula vehicula dapibus. Pellentesque tristique risus lobortis sapien facilisis, nec placerat erat ullamcorper. 
Nam sapien justo, tincidunt id dapibus ac, sollicitudin vel libero. Etiam nec velit aliquam, sollicitudin nisl quis, 
dignissim purus. Nullam id elit id ipsum malesuada posuere. Cras vulputate pulvinar neque vitae tincidunt. Vestibulum 
ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Vestibulum vel risus condimentum, 
posuere lorem eget, tempus mauris. Integer nec iaculis orci, et tincidunt leo. Nullam mi tortor, rhoncus sed interdum 
sed, finibus non magna. Cras tincidunt lectus orci, in rhoncus tellus blandit et. Suspendisse quis condimentum 
lectus. Maecenas odio massa, tincidunt id nunc sed, dapibus lobortis nisi. Suspendisse rhoncus tempus metus. Maecenas 
auctor sem eget ante viverra, ac pharetra diam blandit. Duis euismod feugiat lacus, sit amet posuere quam rutrum non. 
Mauris consectetur lectus ut diam sagittis lobortis. """


counter = {}
for word in Text.split():
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
print(counter, end=' ')
