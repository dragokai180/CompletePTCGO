from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='4ab16c4a-4239-5ad8-8502-ea6bd5f0215f',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokmonBreeder.Name',
    display_name='Pokémon Breeder',
    searchable_by=['Pokémon Breeder', 'Supporter', 'PokmonBreeder'],
    subtypes=['Supporter'],
    collector_number=63,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw 2 cards and heal 20 damage from your Active Pokémon. If you have no cards in your deck, you can't play this card."),
    condition=standard_trainer_condition("Draw 2 cards and heal 20 damage from your Active Pokémon. If you have no cards in your deck, you can't play this card."),
)
