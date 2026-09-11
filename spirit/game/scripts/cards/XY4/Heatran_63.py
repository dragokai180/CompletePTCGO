from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='417db991-8a3b-5781-8d5f-4fd9e7839e24',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name',
    display_name='Heatran',
    searchable_by=['Heatran', 'Basic', 'Heatran'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=485,
    abilities=[
        Attack(
            title='Steel Drop',
            game_text='If there is any Stadium card in play, this attack does 40 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Steam Blast',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
