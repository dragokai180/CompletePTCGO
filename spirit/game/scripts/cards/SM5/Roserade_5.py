from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37bbfdde-b51d-5b3d-ba27-a23422f3e125',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name',
    display_name='Roserade',
    searchable_by=['Roserade', 'Stage 1', 'Roserade'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name',
    family_id=315,
    abilities=[
        Attack(
            title='Inviting Poison',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. The new Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flower Tornado',
            game_text='Move any number of Grass Energy from your Pokémon to your other Pokémon in any way you like.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
