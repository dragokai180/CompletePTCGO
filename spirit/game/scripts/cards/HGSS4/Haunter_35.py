from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3489ea66-224b-51af-9ed3-1628b04cc089',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    display_name='Haunter',
    searchable_by=['Haunter', 'Stage 1', 'Haunter'],
    subtypes=['Stage 1'],
    collector_number=35,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name',
    family_id=92,
    abilities=[
        Attack(
            title='Sneaky Placement',
            game_text="Put 2 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sleep Poison',
            game_text='The Defending Pokémon is now Asleep and Poisoned.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
