from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='46dc8b79-c316-56e5-a836-34e11b81138c',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name',
    display_name='Volcarona',
    searchable_by=['Volcarona', 'Stage 1', 'Volcarona'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name',
    family_id=636,
    abilities=[
        Attack(
            title='Burning Scales',
            game_text='Flip 2 coins. This attack does 20 more damage for each heads.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Wind Wheel',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon."),
)
