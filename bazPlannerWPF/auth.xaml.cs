using System.Windows;
using static bazPlannerWPF.Owner;

namespace bazPlannerWPF
{
    public partial class auth : Window
    {
        public auth()
        {
            InitializeComponent();
        }

        private void AuthToDB(object sender, RoutedEventArgs e)
        {
            ((MainWindow)Application.Current.MainWindow).labelAuth.Content =  Auth(TextBoxUser.Text, TextBoxPassword.Text);
            Close();
        }
    }
}