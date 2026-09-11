from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c2c52cb-51c3-5da5-a799-f226be89032f',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name',
    display_name='Politoed',
    searchable_by=['Politoed', 'Stage 2', 'Politoed'],
    subtypes=['Stage 2'],
    collector_number=25,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    family_id=186,
    abilities=[
        Attack(
            title='Roll Call',
            game_text='Search your deck for a Poliwag, a Poliwhirl, and a Poliwrath, and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hyper Jump',
            game_text='You may shuffle this Pokémon and all cards attached to it into your deck.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
