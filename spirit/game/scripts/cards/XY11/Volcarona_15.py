from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='91aa03bb-8425-55aa-9941-65d3f0a106b0',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name',
    display_name='Volcarona',
    searchable_by=['Volcarona', 'Stage 1', 'Volcarona'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE, PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name',
    family_id=636,
    abilities=[
        Attack(
            title='Shimmering Scales',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused. If tails, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Power Hurricane',
            game_text='Discard all Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
