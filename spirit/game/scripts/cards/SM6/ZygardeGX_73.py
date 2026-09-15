from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b9936c70-2929-54a3-b319-4c3a3755b33d',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeGX.Name',
    display_name='Zygarde-GX',
    searchable_by=['Zygarde-GX', 'Basic', 'GX', 'ZygardeGX'],
    subtypes=['Basic', 'GX'],
    collector_number=73,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=718,
    abilities=[
        Attack(
            title='Cell Connector',
            game_text='Attach 2 Fighting Energy cards from your discard pile to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title="Land's Wrath",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
        Attack(
            title='Verdict-GX',
            game_text="Prevent all damage done to this Pokémon by attacks from Pokémon-GX and Pokémon-EX during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
            locks_next_turn=False,
            gx=True,
        ),
    ],
)
