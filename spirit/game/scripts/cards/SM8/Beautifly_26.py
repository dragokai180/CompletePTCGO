from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e572dd6-20f3-5dc7-83f5-d1e99ddf7828',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name',
    display_name='Beautifly',
    searchable_by=['Beautifly', 'Stage 2', 'Beautifly'],
    subtypes=['Stage 2'],
    collector_number=26,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name',
    family_id=265,
    abilities=[
        Attack(
            title='Skill Dive',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Butterfly Edge',
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
