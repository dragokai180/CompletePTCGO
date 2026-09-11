from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='18d4edf1-4652-569a-baa4-bef6fdff4563',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name',
    display_name='Makuhita',
    searchable_by=['Makuhita', 'Basic', 'Makuhita'],
    subtypes=['Basic'],
    collector_number=112,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=296,
    abilities=[
        Attack(
            title='Slap Push',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
