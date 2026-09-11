from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='96588d52-c4c9-5e2b-bcdb-8e5cee39cf4a',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name',
    display_name='Glameow',
    searchable_by=['Glameow', 'Basic', 'Glameow'],
    subtypes=['Basic'],
    collector_number=159,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=431,
    abilities=[
        Attack(
            title='Caturday',
            game_text='Draw a card. If you do, this Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Boing Boing Tail',
            game_text="This attack does 60 damage to 1 of your opponent's Pokémon-GX or Pokémon-EX. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
