from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe105197-0cc1-5f89-8cc3-4f0692f3b68e',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name',
    display_name='Nidoqueen',
    searchable_by=['Nidoqueen', 'Stage 2', 'Nidoqueen'],
    subtypes=['Stage 2'],
    collector_number=69,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name',
    family_id=29,
    abilities=[
        Attack(
            title='Poison Jab',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Dynamite Punch',
            game_text="This Pokémon does 20 damage to itself. Don't apply Weakness to this damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)"),
)
