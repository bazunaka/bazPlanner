using System.Windows;

namespace bazPlannerWPF
{
    public partial class create_user : Window
    {
       
        public create_user()
        {
            InitializeComponent();
        }

        private void okClick_Click(object sender, RoutedEventArgs e)
        {
            Owner asd = new Owner();
            asd.nameOwner = username.Text;
            asd.passwordOwner = userpswd.Text;

            qwe.Content = asd.nameOwner;
            zxc.Content = asd.passwordOwner;
        }
    }
}
