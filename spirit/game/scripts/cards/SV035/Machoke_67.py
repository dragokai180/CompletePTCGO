from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fd41e9a5-4c78-5e84-8cf5-458a1824e31d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name',
    display_name='Machoke',
    searchable_by=['Machoke', 'Stage 1', 'Machoke'],
    subtypes=['Stage 1'],
    collector_number=67,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name',
    family_id=66,
    abilities=[
        Attack(
            title='Mountain Ramming',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
