from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2f75221c-5a78-594c-b613-a219f50130b1',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name',
    display_name='Breloom',
    searchable_by=['Breloom', 'Stage 1', 'Breloom'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name',
    family_id=285,
    abilities=[
        Attack(
            title='Dynamic Punch',
            game_text="Flip a coin. If heads, this attack does 20 more damage and your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Mega Kick',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
