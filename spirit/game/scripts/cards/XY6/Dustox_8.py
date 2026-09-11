from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10a61659-80c2-54cc-8f15-c002df2487a2',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name',
    display_name='Dustox',
    searchable_by=['Dustox', 'Stage 2', 'Dustox'],
    subtypes=['Stage 2'],
    collector_number=8,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name',
    family_id=265,
    abilities=[
        Attack(
            title='Flap',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title='Wind Shard',
            game_text="This attack does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card."),
)
