from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c90c8df5-ee10-5535-b810-9516d9f52904',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name',
    display_name='Yveltal',
    searchable_by=['Yveltal', 'Basic', 'Yveltal'],
    subtypes=['Basic'],
    collector_number=139,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title='Blow Through',
            game_text='If there is any Stadium card in play, this attack does 20 more damage.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Shadow Impact',
            game_text='Put 3 damage counters on 1 of your Pokémon.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
