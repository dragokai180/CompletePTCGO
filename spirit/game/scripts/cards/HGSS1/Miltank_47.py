from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='04916113-a28d-547c-abad-f7bdb781e38f',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name',
    display_name='Miltank',
    searchable_by=['Miltank', 'Basic', 'Miltank'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=241,
    abilities=[
        Attack(
            title='Moomoo Squeeze',
            game_text='Search your deck for a Moomoo Milk card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Body Slam',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
