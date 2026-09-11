from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7fd85dd0-629f-5500-b932-adc5fca48e60',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name',
    display_name='Clefable',
    searchable_by=['Clefable', 'Stage 1', 'Clefable'],
    subtypes=['Stage 1'],
    collector_number=82,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name',
    family_id=35,
    abilities=[
        Attack(
            title='Moon Barrier',
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to this Pokémon by Dragon Pokémon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Tumbling Attack',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
