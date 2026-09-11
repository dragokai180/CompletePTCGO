from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70bd91f3-c603-5637-a85e-314055a8ab40',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name',
    display_name='Palafin',
    searchable_by=['Palafin', 'Stage 1', 'Palafin'],
    subtypes=['Stage 1'],
    collector_number=62,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name',
    family_id=963,
    abilities=[
        Attack(
            title='Jet Punch',
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Justice Kick',
            game_text="If this Pokémon didn't move from the Bench to the Active Spot this turn, this attack does nothing.",
            cost={PokemonTypes.WATER: 2},
            damage=210,
            effect=standard_attack,
        ),
    ],
)
