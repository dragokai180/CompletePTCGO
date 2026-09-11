from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5fe47fcd-9113-55ca-8f7f-2f8964e503a5',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name',
    display_name='Grimer',
    searchable_by=['Grimer', 'Basic', 'Grimer'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=88,
    abilities=[
        Attack(
            title='Sticky Liquid',
            game_text="During your opponent's next turn, the Defending Pokémon's Retreat Cost is Colorless more.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sludge Toss',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
