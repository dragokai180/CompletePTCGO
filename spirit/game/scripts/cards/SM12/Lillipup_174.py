from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ce8e8515-2966-5788-8fee-960191def74d',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name',
    display_name='Lillipup',
    searchable_by=['Lillipup', 'Basic', 'Lillipup'],
    subtypes=['Basic'],
    collector_number=174,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=506,
    abilities=[
        Attack(
            title='Baby-Doll Eyes',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
