from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b0169faf-989c-509a-9d2c-a419f0ad9518',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mausholdex.Name',
    display_name='Maushold ex',
    searchable_by=['Maushold ex', 'Stage 1', 'ex', 'Mausholdex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=155,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name',
    family_id=924,
    abilities=[
        Ability(
            title='Solidarity',
            game_text="If this Pokémon is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon for each of your Tandemaus, Maushold, and Maushold ex in play.",
            effect=standard_ability,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title='Nom-Nom-Nom Incisors',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
