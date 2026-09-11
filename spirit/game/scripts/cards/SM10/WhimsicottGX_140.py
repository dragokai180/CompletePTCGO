from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0de5f411-3e11-5513-b6c0-06516b5c8831',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WhimsicottGX.Name',
    display_name='Whimsicott-GX',
    searchable_by=['Whimsicott-GX', 'Stage 1', 'GX', 'WhimsicottGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=140,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name',
    family_id=546,
    abilities=[
        Ability(
            title='Fluffy Cotton',
            game_text='If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.',
            passive=standard_passive('If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.'),
        ),
        Attack(
            title='Energy Blow',
            game_text='This attack does 30 more damage times the amount of Energy attached to this Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Toy Box-GX',
            game_text="Search your deck for up to 5 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
