from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c72ee44d-e61b-5e21-920d-f630048b0fa5',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdierex.Name',
    display_name='Bombirdier ex',
    searchable_by=['Bombirdier ex', 'Basic', 'ex', 'Bombirdierex'],
    subtypes=['Basic', 'ex'],
    collector_number=156,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=962,
    abilities=[
        Attack(
            title='Fast Carrier',
            game_text='If you go first, you can use this attack during your first turn. Search your deck for up to 3 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Shadowy Wind',
            game_text='You may put this Pokémon and all attached cards into your hand.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
