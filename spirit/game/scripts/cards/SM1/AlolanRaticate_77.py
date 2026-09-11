from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ac2f4563-74c7-5d3d-b95f-1c0af2c80587',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaticate.Name',
    display_name='Alolan Raticate',
    searchable_by=['Alolan Raticate', 'Stage 1', 'AlolanRaticate'],
    subtypes=['Stage 1'],
    collector_number=77,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name',
    family_id=19,
    abilities=[
        Attack(
            title='Evil Orders',
            game_text='Search your deck for a number of cards up to the number of your Benched Pokémon and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Endeavor',
            game_text='Flip 2 coins. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
