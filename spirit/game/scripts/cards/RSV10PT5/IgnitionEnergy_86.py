from spirit.game.data_utils import EnergyCardDef, Ability, Triggers, def_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.session.passives import Passive, carrier_pokemon


class IgnitionEnergyPassive(Passive):
    """On an Evolution Pokémon, this card provides Colorless Colorless
    Colorless instead of a single Colorless."""

    def modify_energy_provided(self, options, energy, holder, board):
        if carrier_pokemon(energy) is not holder or holder is None:
            return options
        if not is_evolution_pokemon(holder):
            return options
        colorless = PokemonTypes.COLORLESS.value
        return [[colorless, colorless, colorless]]


async def discard_ignition_energy(ctx):
    """At the end of your turn, discard each attached Ignition Energy."""
    to_discard = [
        energy for energy in ctx.attached_energies(ctx.source)
        if getattr(def_for(energy.archetype_id), "display_name", None)
        == "Ignition Energy"
    ]
    if to_discard:
        await ctx.discard_cards(to_discard)


card = EnergyCardDef(
    guid="436e6ceb-6880-56c0-9603-e6d61087579a",
    key="RSV10PT5",
    name="Ignition Energy",
    display_name="Ignition Energy",
    searchable_by=["Ignition Energy","Special","IgnitionEnergy"],
    subtypes=["Special"],
    collector_number=86,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=IgnitionEnergyPassive(),
    granted_abilities=[
        Ability(
            title="Ignition Energy",
            game_text="At the end of your turn, discard this card.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_ignition_energy,
        ),
    ],
)
