from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a52358c3-dbd3-51ef-b34c-f083f2a2e569',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Decidueyeex.Name',
    display_name='Decidueye ex',
    searchable_by=['Decidueye ex', 'Stage 2', 'ex', 'Decidueyeex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=15,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name',
    family_id=722,
    abilities=[
        Ability(
            title='Total Freedom',
            game_text='Once during your turn, you may use this Ability. If this Pokémon is on the Bench, switch it with your Active Pokémon. Or, if this Pokémon is in the Active Spot, switch it with 1 of your Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hunting Arrow',
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
