from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ff592e32-8041-53c4-8f80-130195cd2d06',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmotex.Name',
    display_name='Pawmot ex',
    searchable_by=['Pawmot ex', 'Stage 2', 'ex', 'Pawmotex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=73,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name',
    family_id=923,
    abilities=[
        Attack(
            title='Zap Kick',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Attack(
            title='Levin Strike',
            game_text="Discard 2 Lightning Energy from this Pokémon. This attack does 220 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=standard_attack,
        ),
    ],
)
