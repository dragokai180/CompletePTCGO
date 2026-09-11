from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8daa39c-484f-507b-a1a2-9c95e8244589',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name',
    display_name='Espathra',
    searchable_by=['Espathra', 'Stage 1', 'Espathra'],
    subtypes=['Stage 1'],
    collector_number=81,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name',
    family_id=955,
    abilities=[
        Ability(
            title='Stance',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may prevent all damage from and effects of attacks from your opponent's Pokémon done to this Pokémon until the end of your opponent's next turn.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Glittering Eyes',
            game_text='If Tulip is in your discard pile, this attack does 70 more damage.',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
