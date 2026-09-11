from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e651279d-8a3a-50e6-b9bc-d7418fec9236',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name',
    display_name='Medicham',
    searchable_by=['Medicham', 'Stage 1', 'Medicham'],
    subtypes=['Stage 1'],
    collector_number=81,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name',
    family_id=307,
    abilities=[
        Attack(
            title='Calm Mind',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Yoga Kick',
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)"),
)
