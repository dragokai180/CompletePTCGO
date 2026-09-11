from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fd6819cc-42b1-5a04-835c-2415eb045b8b',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name',
    display_name='Dugtrio',
    searchable_by=['Dugtrio', 'Stage 1', 'Dugtrio'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    family_id=50,
    abilities=[
        Attack(
            title='Earthquake',
            game_text="This attack does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Rock Tumble',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
