from JoKeRUB import l313l

from ..core.managers import edit_or_reply 
@l313l.on(admin_cmd(pattern="الكواكب(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "\n **قائمة كواكب العقرب 🦂 \n \n ✎┊‌ اختر احداها: \n\n- {`.عطارد`} \n- {`.الزهرة`} \n\n- {`.ألأرض`} \n- {`.المريخ`} \n\n- {`.المشتري`} \n- {`.زحل`} \n\n- {`.اورانوس`} \n- {`.نبتون`} \n\n [العقرب | 𝗦𝗰𝗼𝗿𝗽𝗶𝗼](t.me/Scorpions_scorp) 🦂**") 

@l313l.on(admin_cmd(pattern="عطارد(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, " (رمزه: ☿) هو أصغر كواكب المجموعة الشمسية وأقربها إلى الشمس، أطلقت العرب على هذا الكوكب تسمية «عطارد»؛ وأصل الاسم من المصدر ط ر د، طارد ومطّرَد أي المتتابع في سيره، وأيضاً سريع الجري ومن هنا اسم الكوكب عطارد الذي يرمز إلى السرعة الكبيرة لدوران الكوكب حول الشمس. إن اللغات التي لم تعرف الكوكب باسم محدد، تستعمل الاسم اللاتيني ميركوري نسبة لإله التجارة الروماني.")
            
@l313l.on(admin_cmd(pattern="الزهرة(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "الزهرة (رمزه: ♀) هو ثاني كواكب المجموعة الشمسية من حيث المسافة بينه وبين الشمس. يبعد الزهرة عن الشمس نحو 108 مليون كيلومتر، ومَدَارُه حول الشمس ليس دائريًا تمامًا، وهو كوكب ترابي مثل كوكبي عطارد والمريخ، وهو شبيه بكوكب الأرض من حيث الحجم والتركيب. سُمّي فينوس نسبة إلى إلهة الجمال، أما سبب تسميته بالزهرة فبحسب ما ورد في لسان العرب: الزُّهْرَة هي الحسن والبياض، زَهرَ زَهْراً والأَزْهَر أي الأبيض المستنير. والزهرة: البياض النير، ومن هنا سُمّي بكوكب الزُّهَرَة. قال في لسان العرب: (والزُّهَرَة، بفتح الهاء: هذا الكوكب الأَبيض). أي أن اسمه يعود إلى سطوع هذا الكوكب ورؤيته من الكرة الأرضية، وذلك لانعكاس كمية كبيرة من ضوء الشمس بسبب كثافة الغلاف الجوي فيه الكبيرة.")
            
@l313l.on(admin_cmd(pattern="الأرض(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event,  " ألأرض (رمزها: 🜨) هي ثالث كواكب المجموعة الشمسية بعدًا عن الشمس بعد عطارد والزهرة، وتُعتبر من أكبر الكواكب الأرضية وخامس أكبر الكواكب في النظام الشمسي، وذلك من حيث قطرها وكتلتها وكثافتها، ويُطلق على هذا الكوكب أيضًا اسم العالم.")
@l313l.on(admin_cmd(pattern="المريخ(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event,  " المريخ أو الكوكب الأحمر هو الكوكب الرابع من حيث البعد عن الشمس في النظام الشمسي وهو الجار الخارجي للأرض، ويصنف المريخ كوكباً صخرياً، من مجموعة الكواكب الأرضية (الشبيهة بالأرض). أما اسمه بالعربية فهو مُشتق من كلمة «أمرخ» أي صاحب البقع الحمراء، ويقال ثور أَمرخ أي به بقع حمراء، وأما مارس (باللاتينية: Mars) فهو اسم الإله الذي اتخذه الرومان للحرب، وأما لقب الكوكب الأحمر فسببه لون الكوكب المائل إلى الحمرة أو الاحمرار بفعل نسبة غبار أكسيد الحديد الثلاثي العالية على سطحه وفي جوه. يبلغ قطر المريخ حوالي 6792 كم (4220 ميل)، وهو بذلك مساو لنصف قطر الأرض وثاني أصغر كواكب النظام الشمسي بعد عطارد. تقدّر مساحته بربع مساحة الأرض. يدور المريخ حول الشمس في مدار يبعد عنها بمقدار 228 مليون كلم تقريبا، أي 1.5 مرة من المسافة الفاصلة بين مدار الأرض والشمس. يغطي الحوض القطبي الشمالي الأملس نصف الكرة الشمالي تقريباً 40% من الكوكب وقد يكون له تأثير كبير على الكوكب. المريخ له قمران، يسمّى الأول ديموس أي الرعب باللغة اليونانية والثاني فوبوس أي الخوف، وهما صغيران وغير منتظمي الشكل، ويمكن أن يكونا كويكبين قام بالتقاطهما، على غرار 5261 يوريكا، وهو طروادة مريخية.")
@l313l.on(admin_cmd(pattern="المشتري(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "المشتري هو أضخم كواكب المجموعة الشمسية. سمي بالمشتري لأنه يستشري في سيره أي يلـجُّ ويمضي ويَـجِدُّ فيه بلا فتور ولا انكسار. وكان المشتري معروفاً للفلكيين القدماء وارتبط بأساطير وأديان العديد من الشعوب. وقد أطلق الرومان عليه اسم جوبيتر وهو إله السماء والبرق. ويظهر المشتري من الأرض بسطوع كبير فيبلغ قدره الظاهري −2.94 مما يجعله ثالث الأجرام تألقاً في سماء الليل بعد القمر والزهرة")
@l313l.on(admin_cmd(pattern="زحل(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, " (رمزه: ♄)، واسمه مشتق من الجذر «زَحَل» بمعنى تنحّى وتباعد. ويُقال أنه سمي زُحَل لبعده في السماء، أما الإسم اللاتيني فهو «ساتورن» وهو إله الزراعة والحصاد عند الرومان، ويُمثل رمزه منجل الإله الروماني سالف الذكر  هو الكوكب السادس من حيث بُعدُهُ عن الشمس وهو ثاني أكبر كوكب في النظام الشمسي بعد المشتري، ويُصنّف زحل ضمن الكواكب الغازية مثل المشتري وأورانوس ونبتون. وهذه الكواكب الأربعة معاً تُدعى «الكواكب الجوفيانية» بمعنى «أشباه المشتري». نصفُ قطر هذا الكوكب أضخمُ بتسع مرّات من نصف قطر الأرض، إلا أن كثافته تصل إلى ثمن كثافة الأرض، أما كتلته فتفوق كتلة الأرض بخمس وتسعين مرة.")
@l313l.on(admin_cmd(pattern="اورانوس(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "أورانوس (رمزه: ⛢) هو سابع الكواكب بعدًا عن الشمس، وثالث أضخم كواكب المجموعة الشمسية، والرابع من حيث الكتلة. سمي على اسم الإله أورانوس (باليونانية القديمة: Οὐρανός) في الميثولوجيا الإغريقية. لم يتم تمييزه من قبل الحضارات القديمة على أنه كوكب رغم أنه مرئي بالعين المجردة، نظرًا لبهوته وبطء دورانه في مداره. أعلن وليام هرشل عن اكتشافه في 13 آذار/مارس من سنة 1781، موسعًا بذلك حدود الكواكب المعروفة لأول مرة في التاريخ. كما كان أورانوس أول كوكب يُكتشف من خلال التلسكوب.")
@l313l.on(admin_cmd(pattern="نبتون(?: |$)(.*)"))
async def _(event):
    await edit_or_reply(event, "نبتون Neptune (رمزه: ♆) معناها بالإغريقية إله الماء، ويطلق عليه الكوكب الأزرق هو أحد كواكب النظام الشمسي وهو رابع أكبر الكواكب الثمانية، وهو ثامن كواكب المجموعة الشمسية وأبعدها عن الشمس في النظام الشمسي وهو رابع أكبر كوكب نسبةً إلى قطره وثالث أكبر كوكب نسبةً إلى كتلته. تبلغ كتلة نبتون 17 مرة كتلة الأرض. وهو أكبر قليلًا من توأمه القريب أورانوس الذي يعادل 15 مرة كتلة الأرض. يكمل نبتون دورة واحدة حول الشمس كل 164.8 سنة في معدل مسافة حوالي 30.1 وحدة فلكية (4.5 مليار كم). سمي نبتون نسبةً إلى إله الماء والبحر في الميثولوجيا الرومانية (نيبتون) حيث تم اكتشافه في 23 سبتمبر عام 1846.")
