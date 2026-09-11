from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5c2bd2a8-d8dd-5829-aa56-9b4297270304',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name',
    display_name='Delcatty',
    searchable_by=['Delcatty', 'Stage 1', 'Delcatty'],
    subtypes=['Stage 1'],
    collector_number=114,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name',
    family_id=300,
    abilities=[
        Attack(
            title='Replace',
            game_text='Move as many Energy attached to your Pokémon to your other Pokémon in any way you like.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Play Rough',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
