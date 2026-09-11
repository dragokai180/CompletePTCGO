from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d6ca9c71-8c5b-5131-a833-f2bb4d89363f',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name',
    display_name='Brionne',
    searchable_by=['Brionne', 'Stage 1', 'Brionne'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name',
    family_id=728,
    abilities=[
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Disarming Voice',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
