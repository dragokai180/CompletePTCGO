from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0f36b954-52b7-5319-b31c-6eb24ed80ff6',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    display_name='Chansey',
    searchable_by=['Chansey', 'Basic', 'Chansey'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=113,
    abilities=[
        Attack(
            title='Scrunch',
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Double-Edge',
            game_text='This Pokémon does 80 damage to itself.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
