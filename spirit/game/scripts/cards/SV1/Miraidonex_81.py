from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5fa18425-ba84-5211-9011-61f159e62c05',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name',
    display_name='Miraidon ex',
    searchable_by=['Miraidon ex', 'Basic', 'ex', 'Miraidonex'],
    subtypes=['Basic', 'ex'],
    collector_number=81,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=1008,
    abilities=[
        Ability(
            title='Tandem Unit',
            game_text='Once during your turn, you may search your deck for up to 2 Basic Lightning Pokémon and put them onto your Bench. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Photon Blaster',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=standard_attack,
        ),
    ],
)
