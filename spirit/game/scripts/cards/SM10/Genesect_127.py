from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3131e20f-7008-5449-93fb-2b9725436107',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Genesect.Name',
    display_name='Genesect',
    searchable_by=['Genesect', 'Basic', 'Genesect'],
    subtypes=['Basic'],
    collector_number=127,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=649,
    abilities=[
        Ability(
            title='Fast-Flight Configuration',
            game_text='If your opponent has any Pokémon-GX or Pokémon-EX in play, this Pokémon has no Retreat Cost.',
            passive=standard_passive('If your opponent has any Pokémon-GX or Pokémon-EX in play, this Pokémon has no Retreat Cost.'),
        ),
        Attack(
            title='Splitting Beam',
            game_text="This attack does 30 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
