from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ddcd5658-1aa7-58c2-998e-c21f725d3489',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name',
    display_name='Throh',
    searchable_by=['Throh', 'Basic', 'Throh'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=538,
    abilities=[
        Attack(
            title='Reverse Shoulder Throw',
            game_text='If your Benched Pokémon have any damage counters on them, this attack does 90 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
