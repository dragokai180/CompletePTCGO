from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e1ff831-8ed1-58e1-b7c0-0490d6466556',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name',
    display_name='Luxray',
    searchable_by=['Luxray', 'Stage 2', 'Luxray'],
    subtypes=['Stage 2'],
    collector_number=71,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name',
    family_id=403,
    abilities=[
        Ability(
            title='Swelling Flash',
            game_text='Once during your turn, if this Pokémon is in your hand and you have more Prize cards remaining than your opponent, you may put this Pokémon onto your Bench.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
            usable_from='hand',
        ),
        Attack(
            title='Wild Charge',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
