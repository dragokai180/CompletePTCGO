from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='68edbde5-8fd4-5645-a170-3689993aff8c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name',
    display_name='Kilowattrel',
    searchable_by=['Kilowattrel', 'Stage 1', 'Kilowattrel'],
    subtypes=['Stage 1'],
    collector_number=79,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name',
    family_id=940,
    abilities=[
        Attack(
            title='Skill Dive',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Thunder Blast',
            game_text='Discard a Lightning Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
