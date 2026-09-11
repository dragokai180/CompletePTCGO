from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='415930a8-3202-581b-a484-9b3c6a10dc36',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name',
    display_name='Floatzel',
    searchable_by=['Floatzel', 'Stage 1', 'Floatzel'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    family_id=418,
    abilities=[
        Ability(
            title='Water Acceleration',
            game_text="Once during your turn (before your attack), you may attach a Water Energy card from your hand to Floatzel. This power can't be used if Floatzel is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Waterfall',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
