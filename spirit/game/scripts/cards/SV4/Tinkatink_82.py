from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d797cf2-5bd0-5393-a11c-0204cf2b236f',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name',
    display_name='Tinkatink',
    searchable_by=['Tinkatink', 'Basic', 'Tinkatink'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=957,
    abilities=[
        Attack(
            title='Mountain Scrounging',
            game_text="Look at the top card of your deck. You may put that card into your hand. If you don't, discard that card and draw a card.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mumble',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
