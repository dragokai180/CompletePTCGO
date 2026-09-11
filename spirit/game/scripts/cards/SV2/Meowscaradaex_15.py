from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc30ea9d-0c6e-5815-a551-910b01910fba',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowscaradaex.Name',
    display_name='Meowscarada ex',
    searchable_by=['Meowscarada ex', 'Stage 2', 'ex', 'Meowscaradaex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=15,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name',
    family_id=906,
    abilities=[
        Ability(
            title='Bouquet Magic',
            game_text="You must discard a Basic Grass Energy card from your hand in order to use this Ability. Once during your turn, you may put 3 damage counters on 1 of your opponent's Benched Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Scratching Nails',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
