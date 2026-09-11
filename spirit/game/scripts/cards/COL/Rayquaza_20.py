from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f3e5527-228e-51d4-8b45-adf30cc52604',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name',
    display_name='Rayquaza',
    searchable_by=['Rayquaza', 'Basic', 'Rayquaza'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=384,
    abilities=[
        Attack(
            title='Inferno Spear',
            game_text='Discard a Fire Energy and a Lightning Energy attached to Rayquaza.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
