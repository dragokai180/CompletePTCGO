from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9f2e13ca-06b2-5733-998a-00607e70d828',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name',
    display_name='Heliolisk',
    searchable_by=['Heliolisk', 'Stage 1', 'Heliolisk'],
    subtypes=['Stage 1'],
    collector_number=44,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name',
    family_id=694,
    abilities=[
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Raging Thunder',
            game_text="This attack does 30 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
