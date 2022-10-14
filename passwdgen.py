            def generatePassword():
                var result           = ''
                var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
                var charactersLength = characters.length
                for  var i = 0; i < 16; i++ :
                  result += characters.charAt(Math.floor(Math.random() * charactersLength))

               return result;