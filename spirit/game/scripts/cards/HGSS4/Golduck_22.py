from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d851e2d0-b36f-5368-854a-d754439cf9c1',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name',
    display_name='Golduck',
    searchable_by=['Golduck', 'Stage 1', 'Golduck'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name',
    family_id=54,
    abilities=[
        Ability(
            title='Natural Remedy',
            game_text='Whenever you attach a Water Energy card from your hand to Golduck, remove 2 damage counters from Golduck.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('Whenever you attach a Water Energy card from your hand to Golduck, remove 2 damage counters from Golduck.'),
        ),
        Attack(
            title='Powerful Splash',
            game_text='Does 30 damage plus 10 more damage for each Water Energy attached to all of your Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
