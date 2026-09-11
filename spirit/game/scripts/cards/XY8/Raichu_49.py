from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='58fe1615-9c6d-516d-8141-16f4cc1dc751',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name',
    display_name='Raichu',
    searchable_by=['Raichu', 'Stage 1', 'Raichu'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    family_id=25,
    abilities=[
        Attack(
            title='Thunderclap Shot',
            game_text="This attack does 50 damage to each of your opponent's Pokémon-EX. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electrosmash',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
