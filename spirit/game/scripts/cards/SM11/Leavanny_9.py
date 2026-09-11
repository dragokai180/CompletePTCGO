from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a9e49a50-a5cf-5e3d-a960-0b9d371a7a91',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name',
    display_name='Leavanny',
    searchable_by=['Leavanny', 'Stage 2', 'Leavanny'],
    subtypes=['Stage 2'],
    collector_number=9,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name',
    family_id=540,
    abilities=[
        Ability(
            title='Blanket Weaver',
            game_text="Your Grass Pokémon take 40 less damage from your opponent's attacks (after applying Weakness and Resistance). You can't apply more than 1 Blanket Weaver Ability at a time.",
            passive=standard_passive("Your Grass Pokémon take 40 less damage from your opponent's attacks (after applying Weakness and Resistance). You can't apply more than 1 Blanket Weaver Ability at a time."),
        ),
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
